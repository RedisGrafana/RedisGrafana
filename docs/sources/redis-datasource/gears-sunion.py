gb = GB('CommandReader')
gb.flatmap(lambda x:  execute('SUNION',*x[1].split(",")))
gb.register(trigger='SUNION')
