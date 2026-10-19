"""Audit tracked source, all reachable commits and package members; never print matching data."""
from pathlib import Path
import re,subprocess,sys,tarfile
root=Path(__file__).resolve().parent.parent
rules={
 'credential-like-token':re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{24,}|sk-[A-Za-z0-9_-]{24,})'),
 'private-key':re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
 'personal-machine-path':re.compile(rb'/(?:Users|home)/[a-z][a-z0-9_-]+/|[a-z0-9-]+\.tail[a-z0-9]+\.ts\.net'),
 'credential-url':re.compile(rb'https?://[^\s"\x27<>]+[?&](?:token|api_key|access_token)=[A-Za-z0-9._~-]{16,}'),
}
allowed_dirs={'src','test','test-support','scripts','docs','.github'}
allowed_root={'AGENTS.md','.gitignore','.gitattributes','README.md','README.en.md','README.zh.md','LICENSE','NOTICE','COMPATIBILITY.md','CHANGELOG.md','CONTRIBUTING.md','SECURITY.md','package.json','package-lock.json','index.mjs','config.schema.json','cordis.patch.yml','cordis.patch.example.yml'}
findings=[];count=0

def inspect(path,data):
 global count
 count+=1
 parts=Path(path).parts
 if (len(parts)==1 and path not in allowed_root) or (len(parts)>1 and parts[0] not in allowed_dirs):findings.append((path,'source-allowlist'))
 if any(p in {'node_modules','fixture','profiles','sessions','artifacts','evidence'} or p.startswith('.dsh') for p in parts):findings.append((path,'runtime-path'))
 for label,pattern in rules.items():
  if pattern.search(data):findings.append((path,label))

paths=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=root).split(b'\0')
for raw in paths:
 if not raw:continue
 path=raw.decode();file=root/path
 if file.is_symlink():findings.append((path,'symlink'));continue
 inspect(path,file.read_bytes())
commits=subprocess.check_output(['git','rev-list','--all'],cwd=root,text=True).splitlines()
for commit in commits:
 metadata=subprocess.check_output(['git','show','-s','--format=%ae%n%ce',commit],cwd=root).splitlines()
 if any(not line.endswith(b'@users.noreply.github.com') for line in metadata):findings.append((commit,'non-public-author'))
 tree=subprocess.check_output(['git','ls-tree','-rz',commit],cwd=root).split(b'\0')
 for record in tree:
  if not record:continue
  meta,path=record.split(b'\t',1);mode,kind,oid=meta.split(b' ')
  if mode==b'120000':findings.append((path.decode(),'historical-symlink'))
  if kind==b'blob':inspect(path.decode(),subprocess.check_output(['git','cat-file','blob',oid.decode()],cwd=root))
for package in (root/'artifacts').glob('*.tgz'):
 with tarfile.open(package,'r:gz') as archive:
  for member in archive.getmembers():
   if not member.isfile() or not member.name.startswith('package/') or '..' in Path(member.name).parts:findings.append((package.name,'unsafe-member'));continue
   inspect(member.name.removeprefix('package/'),archive.extractfile(member).read())
for path,label in findings:print(f'{label}: {path}')
print(f'Audited {count} source/history/package records across {len(commits)} commits; {len(findings)} findings')
sys.exit(bool(findings))
