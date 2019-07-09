class AuctionException(Exception): pass
def main():
    try:
        # 使用try...except来捕捉异常
        # 此时即使程序出现异常，也不会传播给main函数
        mtd('sdf')
    # except AuctionException as ae:
    #     print('自定义异常:', ae) 
    except Exception as e:
        print('程序出现异常:', e)
    # 不使用try...except捕捉异常，异常会传播出来导致程序中止
    mtd(3)
def mtd(a):
    try:
        d = float(a)
        # if a > 0:
        #    raise AuctionException("a的值大于0，不符合要求")
    except Exception as e:
        print('捕捉方法产生的异常：', e)
        #raise AuctionException("a的值大于0，不符合要求")
        #raise ValueError("a的值大于0，不符合要求")
        raise Exception("a的值大于0，不符合要求")
    
main()