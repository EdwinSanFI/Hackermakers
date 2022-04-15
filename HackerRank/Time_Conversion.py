def timeConversion(s):
    if "AM" in s:
        hour = s.split(":",2)
        if hour[0] == '12':
            final = '00' + ":" + hour[1] + ":" + hour[2][:2]
            return final
        else:
            return(hour[0] + ":" + hour[1] + ":" + hour[2][:2])
    else:
        hour = s.split(":", 2)
        if hour[0] == '12':
            return(hour[0] + ":" + hour[1] + ":" + hour[2][:2])
        else:
            hour[0] = int(hour[0]) + 12
            final = str(hour[0]) + ":" + hour[1] + ":" + hour[2][:2]
            return(str(final))

if __name__ == '__main__':
    test1 = '12:40:22AM'
    result = timeConversion(test1)
    # Expected output: 00:40:22
    print(result)

    # test2 = '12:45:54PM'
    # Expected output: 12:45:54

    # test8 = '12:00:00AM'
    # Expected output: 00:00:00

    # test5 = '02:34:50PM'
    # Expected output: 14:34:50