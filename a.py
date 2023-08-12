# reverse a string

'''s = "yash"
ans = ""
n = len(s)
for i in range(len(s)):
    ans = ans + s[n - 1]
    n -= 1

print(ans)

# sql command

select count(*), month from table1
group by month; '''


# count repeated words

'''
s = "i like apple and apple"
l = s.split(" ")
ans = {}
for i in l:
    if i in ans.keys():
        ans[i] += 1
    else:
        ans.update({i:1})
m = set(l)
for i in m:
    if ans[i] > 1:
        print(i, "=", ans[i])'''


# remove hyphens and spaces and create new format sring
n = ""
m = ""
for i in n:
    if i != "-" and i != " ":
        m = m + i
print(m)
ans = ""
count = 0
for i in m:
    ans += i
    count = (count + 1) % 3
    if count % 3 == 0:
        ans += "-"
    if len(ans) > 0:
        if ans[-1] == "-":
            ans = ans[:-1]
print(ans)
