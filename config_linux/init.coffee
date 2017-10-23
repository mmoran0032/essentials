# Edits update the path so that python is found when not launching from bash

# To have a dialogue window showing your path
# alert(process.env.PATH)
process.env.PATH = [
    '/opt/miniconda3/bin',
    process.env.PATH,
    '/home/mikemoran/.local/bin'
].join(':')
