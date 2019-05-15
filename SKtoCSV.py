import re

out=open("DataFiles\SKBdays.csv","w+", encoding="utf8")
with open("DataFiles\SKBdays.txt", "r", encoding="utf8") as f:
    content = f.read().rstrip(' ')
    f.close()
    r = re.sub(r'\s(–|-)\s', r',', content) #take out hyphen, replace with ,
    g = re.sub(r'(Muhammad)(\s)', r'\g<1>,', r) #this is a fix for an outlier
    s = re.sub(r'(\d{1,2})(rd|th|st|nd)(\s)', r'\1 ', g) #take out suffixes from dates
    t = re.sub(r'(,)(\d{1}\s)', r'\g<1>0\2', s) #add a 0 before single digit dates
    x = re.sub(r'\d{4}\s*', r'\n',t) #take years out
    out.write(x)
