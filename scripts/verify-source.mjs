import {readFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
const root=new URL('../',import.meta.url)
const manifest=JSON.parse(await readFile(new URL('docs/source-manifest.json',root),'utf8'))
for(const [path,expected] of Object.entries(manifest.files)){
  const actual=createHash('sha256').update(await readFile(new URL(path,root))).digest('hex')
  if(actual!==expected)throw Error(`Runtime source differs from the recorded extraction: ${path}`)
}
console.log(`Verified ${Object.keys(manifest.files).length} unchanged Bridge runtime files from ${manifest.commit}`)
