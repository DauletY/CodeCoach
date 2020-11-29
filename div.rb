int = gets.to_i
string = gets.to_s
strSpl = string.split(' ')
for i in strSpl
    if(int % i.to_i == 0)
        print 'divisible by all'
        break
    else
        print 'not divisible by all'
        break
    end
end





