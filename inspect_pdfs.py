import pathlib
from PyPDF2 import PdfReader
for name in ['ERD.pdf','UseCase.pdf','Архитектурная схема.pdf']:
    p = pathlib.Path(name)
    if not p.exists():
        print(f'{name}: MISSING')
        continue
    r = PdfReader(str(p))
    print(f'=== {name} pages {len(r.pages)} ===')
    for i, page in enumerate(r.pages[:3]):
        txt = page.extract_text() or ''
        print(f'--- page {i+1} ---')
        print(txt)
