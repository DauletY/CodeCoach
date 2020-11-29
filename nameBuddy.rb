
a = gets.to_s
b = gets.to_s

flag = 0

for i in 0...a.length
    if a[i] == b[0]
        flag = 1
        break
    end
end

if flag == 1
    print 'Compare notes'
else
    print 'No such luck'
end


###############################################
# Text decompressor

S = ['1', '2', '3','4','5','6','7','8','9','0']
for i in 0...a.length
    b = a[i]
    l = a[i-1]
    if S[b.to_i] != ""
        h = b.to_i
        print (l * h)
    end
end
################################################