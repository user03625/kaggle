from kaggle_environments import make

env = make("kore_fleets",debug=True)

#print(env.name,env.version)

env.run(["/home/bz/kaggle/kore/test.py"])
#env.render(mode="human", width=1000, height=800)
out = env.render(mode="ansi")
print(out)
