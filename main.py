example={
  "név1":"def1",
  "név2":"def2",
  "név3":"def3",
  "név4":"def4",
  "név5":"def5",
}
ent=""
for x,y in example.items():
  print(x)
  ent=input("definition: ")
  if(ent==""):
    print(y,"\n")
  else:
    print("wrong button")