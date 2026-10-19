import {execFileSync} from 'node:child_process'
import {mkdir,readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
const root=new URL('../',import.meta.url),out=new URL('artifacts/',root)
const git=(...args)=>execFileSync('git',args,{cwd:root,encoding:'utf8'}).trim()
if(git('status','--porcelain','--untracked-files=normal'))throw Error('Commit source, tests and documentation before packaging')
const commit=git('rev-parse','HEAD'),manifest=JSON.parse(await readFile(new URL('package.json',root),'utf8'))
execFileSync(process.execPath,['scripts/verify-source.mjs'],{cwd:root,stdio:'inherit'})
await mkdir(out,{recursive:true})
const [packed]=JSON.parse(execFileSync('npm',['pack','.','--ignore-scripts','--json','--pack-destination',out.pathname],{cwd:root,encoding:'utf8'}))
if(JSON.stringify(packed.files.map(file=>file.path).sort())!==JSON.stringify(['package.json',...manifest.files].sort()))throw Error('Archive members differ from the explicit package allowlist')
if(git('status','--porcelain','--untracked-files=normal')||git('rev-parse','HEAD')!==commit)throw Error('Source changed during packaging')
const sha256=createHash('sha256').update(await readFile(new URL(packed.filename,out))).digest('hex')
const release={name:manifest.name,version:manifest.version,commit,filename:packed.filename,sha256}
await writeFile(new URL('SHA256SUMS',out),`${sha256}  ${packed.filename}\n`)
await writeFile(new URL('release.json',out),JSON.stringify(release,null,2)+'\n')
console.log(JSON.stringify(release))
