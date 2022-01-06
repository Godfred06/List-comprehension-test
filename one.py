st= '''Hello, I'm the supervillain behind Plantedd. We're an online market for plant lovers plotting to take over the world by making it simple to find and buy plants'''
lst= st.split()
print (lst)
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def clear_punc(lists):
    new_st=''
    new_list=[]
    for word in lists:
        if word[-1] in punctuation_chars:
            new_st=word.replace(word[-1], '')
        else:
            new_st= word
        new_list.append(new_st)
    return new_list


def longlenghts(strings):
    final_list =[string for string in strings if len(string)>=4]
    return final_list
print (clear_punc(lst))
print(longlenghts(clear_punc(lst)))
