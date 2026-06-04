def square_root_bisection(n, tolerance = 0.01, max_iteration = 20):
    if n < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif n == 0 or n == 1:
        print(f"The square root of {n} is {n}")
        return n
    else:
        low = 0
        high = max(1, n)

        for i in range(max_iteration):
            mid = (low + high) / 2
            if i == max_iteration - 1:
                if abs(mid * mid - n) <= tolerance:
                    print(f"The square root of {n} is approximately {mid}")
                    return mid
            if abs(high - low) <= tolerance:
                print(f"The square root of {n} is approximately {mid}")
                return mid
            elif mid * mid > n:
                high = mid
            elif mid * mid < n:
                low = mid

    print(f"Failed to converge within {max_iteration} iterations")
    return None


def main():
    print(square_root_bisection(0))
    print(square_root_bisection(0.001, 1e-7, 50))
    print(square_root_bisection(0.25, 1e-7, 50))
    print(square_root_bisection(1))
    print(square_root_bisection(81, 1e-3, 50))
    print(square_root_bisection(225, 1e-3, 100))
    print(square_root_bisection(225, 1e-7, 100))
    print(square_root_bisection(225, 1e-7, 10))


if __name__ == "__main__":
    main()
