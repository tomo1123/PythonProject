class Cal(object):
    def add_num_and_double(self, x, y):
        result = x + y
        result *= 2
        return result
      
if __name__ == '__main__':
    import doctest
    doctest.testmod()