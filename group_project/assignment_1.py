def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'
    
def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'  



def first_half(a_string):
    # earlier, there is no len() here ... 
    if len(a_string) % 2 > 0:
        return(a_string[:(len(a_string)/2+1)])
    else:
        return(a_string[:(len(a_string)/2)])
        
"""
So, basically i have converted your codes into function.. 
all codes should be inside the function.. 
then your tests will call the function..
Make sense?
"""