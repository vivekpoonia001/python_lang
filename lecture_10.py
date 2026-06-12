'''regular exprrsiion 
there we use search operation
and for all number we use findall '''
import re
# st = r"[6-9]{1}\d{9}"
# str = "9934474889, and 2345823, 8978654378 , 2928273645, 34445"
# print(re.search(pattern=st, string = str))
# print(re.findall(pattern = st, string = str))
st1 = r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z]{2,7}"
str1 = "vivekpoonia2005@gmail.cmoom, rtgt4h52@.in"
print(re.search(pattern = st1, string = str1))