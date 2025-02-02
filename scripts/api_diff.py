from bs4 import BeautifulSoup
import requests
import re
#import difflib

baseline_version = 'v6.3.0'

stable = requests.get('https://casadocs.readthedocs.io/en/%s/genindex.html' % baseline_version).text
stable_soup = BeautifulSoup(stable, 'html.parser')
stable_set = stable_soup.find_all('a')

tasklist, toollist, shelllist, datalist, lithlist, conflist = [], [], [], [], [], []
for ll in stable_set:
    page = ll.get('href')
    if 'casadata' in page:
        datalist += [re.sub('.*?\#(casadata\..+?)+', r'\1', page, flags=re.DOTALL).replace('/', '.')]
    if 'casalith' in page:
        lithlist += [re.sub('.*?\#(casalith\..+?)?', r'\1', page, flags=re.DOTALL).replace('/', '.')]
    if 'configuration' in page:
        conflist += [re.sub('.*?\#(configuration\..+?)?', r'\1', page, flags=re.DOTALL).replace('/', '.')]

    if not '.html' in page: continue
    task = re.sub('.*?(casatasks\..+?\..+?)?\.html.*', r'\1', page, flags=re.DOTALL)
    tool = re.sub('.*?(casatools\..+?)?\.html.*', r'\1', page, flags=re.DOTALL)
    shell = re.sub('.*?(casashell/.+?)?\.html.*', r'\1', page, flags=re.DOTALL).replace('/','.')
    if len(task) > 0: tasklist += [task]
    if len(tool) > 0: toollist += [tool]
    if len(shell) > 0: shelllist += [shell]


ostr = ''
for task in sorted(tasklist):
    print(task)
    stable = requests.get('https://casadocs.readthedocs.io/en/%s/_modules/%s.html' % (baseline_version, task.replace('.', '/'))).text
    stable_soup = BeautifulSoup(stable, 'html.parser')
    stable_spec = stable_soup.find(id=task.split('.')[-1]).get_text().strip()
    stable_spec = re.sub('\[docs\]def\s|\:\s*.*', '', stable_spec, flags=re.DOTALL).replace('\n','')
    ostr += '.'.join(task.split('.')[:2]) + '.' + stable_spec + '\n'


for tool in set(toollist):
    print(tool)
    stable = requests.get('https://casadocs.readthedocs.io/en/%s/_modules/%s.html' % (baseline_version, tool.replace('.', '/'))).text
    stable_soup = BeautifulSoup(stable, 'html.parser')
    stable_methods = stable_soup.find_all(id=re.compile(tool.split('.')[-1]+'\..+'))
    for method in stable_methods:
        stable_spec = method.get_text()
        stable_spec = re.sub('\[docs\]\s*def\s|\)\:\s+.*', '', stable_spec, flags=re.DOTALL).replace('\n', '') + ')'
        ostr += tool + '.' + stable_spec + '\n'


for shell in set(shelllist):
    print(shell)
    stable = requests.get('https://casadocs.readthedocs.io/en/%s/_sources/api/%s.rst.txt' % (baseline_version, shell.replace('.', '/'))).text
    stable_spec = re.search('\.\. function:: (.+?)\n', stable, flags=re.DOTALL)
    stable_spec = re.search('\.\. data:: (.+?)\n', stable, flags=re.DOTALL).group(1) if stable_spec is None else stable_spec.group(1)
    ostr += 'casashell.' + stable_spec + '\n'


stable = requests.get('https://casadocs.readthedocs.io/en/%s/api/casalith.html' % (baseline_version)).text
stable_soup = BeautifulSoup(stable, 'html.parser')
for lith in set(lithlist):
    print(lith)
    stable_spec = stable_soup.find(id=lith).get_text().strip()[:-2] #.replace('Â','')
    ostr += 'casalith.' + stable_spec + '\n'


stable = requests.get('https://casadocs.readthedocs.io/en/%s/api/casadata.html' % (baseline_version)).text
stable_soup = BeautifulSoup(stable, 'html.parser')
for data in set(datalist):
    print(data)
    stable_spec = stable_soup.find(id=data).get_text().strip()[:-2] #.replace('Â','')
    ostr += 'casadata.' + stable_spec + '\n'


stable = requests.get('https://casadocs.readthedocs.io/en/%s/api/configuration.html' % (baseline_version)).text
stable_soup = BeautifulSoup(stable, 'html.parser')
for conf in set(conflist):
    print(conf)
    stable_spec = stable_soup.find(id=conf).get_text().strip()[:-2] #.replace('Â','')
    ostr += 'configuration.' + stable_spec + '\n'


with open('api_baseline.txt', 'w') as fid:
    fid.write(baseline_version + '\n\n' + ostr)




#bname = 'cas-13144'
#branch = requests.get('https://casadocs.readthedocs.io/en/%s/genindex.html' % bname).text
#branch_soup = BeautifulSoup(branch, 'html.parser')
#branch_set = branch_soup.find_all('a')
#union_set = list(set(stable_set + branch_set))

# tasklist = []
# for ll in union_set:
#    page = ll.get('href')
#    if not '.html' in page: continue
#    task = re.sub('.*?(casatasks\..+?\..+?)?\.html.*', r'\1', page, flags=re.DOTALL)
#    if len(task) > 0: tasklist += [task]

# dd = difflib.Differ()
#for task in sorted(tasklist):
    # print(task)
    
    # branch = requests.get('https://casadocs.readthedocs.io/en/%s/api/tt/%s.html' % (bname, task)).text
    # branch_soup = BeautifulSoup(branch, 'html.parser')
    # branch_spec = branch_soup.find(id=task).get_text().strip()
    # branch_spec = re.sub('\[source\].*', '', branch_spec, flags=re.DOTALL)

    # task_diff = '\n'.join(dd.compare([stable_spec], [branch_spec]))
    # if not task_diff.startswith(' '):
    #    print(task_diff,'\n')






#def show_diff(seqm):
#    output= []
#    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
#        if opcode == 'equal':
#            output.append(seqm.a[a0:a1])
#        elif opcode == 'insert':
#            output.append("<b>" + seqm.b[b0:b1] + "</b>")
#        elif opcode == 'delete':
#            output.append("<del>" + seqm.a[a0:a1] + "</del>")
#        elif opcode == 'replace':
#            output.append("<b>" + seqm.a[a0:a1] + "</b>")
#    return ''.join(output)

#sm = difflib.SequenceMatcher(None, stable_spec, branch_spec)
#with open('diff.html', 'w') as fid:
#    fid.write(show_diff(sm))


#diffs = difflib.HtmlDiff().make_file([stable_spec], [branch_spec])
#with open('diff.html', 'w') as fid:
#    fid.write(diffs)

#difflib.Differ(None, stable_spec, branch_spec).get_matching_blocks()