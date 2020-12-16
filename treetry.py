import nltk
groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
'Open' -> 'Google'|'app'
'Tap' -> 'Edit'|'icon'|'screen'|'video'
'access' -> 'Edit' | 'options'
""")
print(groucho_dep_grammar)

pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = ['Open Google Photos app and search for the video you want to edit',
'Tap video you want to edit to open it',
'Tap screen outside of the video to display the editing options',
'Tap Edit icon, to access the Edit options',
'Tap Save copy in the upper-right corner to save the video',
'Tap pencil icon in the lower-left corner',
'Add filter',
'Add stickers and emoji']

tree = pdp.parse(sent)
print(tree)

