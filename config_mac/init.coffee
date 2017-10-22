# Edits update the path so that python is found when not launching from bash

# To have a dialogue window showing your path
# alert(process.env.PATH)
process.env.PATH = [
    process.env.PATH,
    '/Users/michamor/.local/bin'
].join(':')

# alert(process.env.PATH)
