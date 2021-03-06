import mysql.connector


def main():

    my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="minerva"
        )

    my_cursor = my_db.cursor()

    # Clean current data
    my_cursor.execute("DELETE FROM geodata")
    my_cursor.execute("DELETE FROM intercepts")

    github_data_1 = \
    [-122.39116,37.78242,
    -122.38981,37.78135,
    -122.38976,37.7813,
    -122.38982,37.78125,
    -122.38998,37.78113,
    -122.39017,37.78097,
    -122.39037,37.78081,
    -122.39044,37.78076,
    -122.39054,37.78068,
    -122.3906,37.78073,
    -122.39079,37.78088,
    -122.39168,37.78158,
    -122.39202,37.78186,
    -122.3913,37.78244]

    github_data_2 = \
    [-122.39554,37.78155,
    -122.39477,37.78217,
    -122.39471,37.78222,
    -122.39421,37.78264,
    -122.3937,37.78307,
    -122.39342,37.78284,
    -122.39335,37.78279,
    -122.39313,37.78264,
    -122.39291,37.78247,
    -122.39285,37.78242,
    -122.39265,37.78227,
    -122.39215,37.78186,
    -122.39266,37.78146,
    -122.39321,37.78101,
    -122.39328,37.78096,
    -122.39364,37.78066,
    -122.39431,37.78017,
    -122.39457,37.78036,
    -122.39463,37.78041,
    -122.39501,37.78073,
    -122.39507,37.78078,
    -122.39516,37.78085,
    -122.39546,37.78109,
    -122.39553,37.78114,
    -122.39579,37.78135,
    -122.39571,37.78141,]

    github_data_3 = \
    [
      -122.39515,
      37.78197,
      -122.3948,
      37.78225,
      -122.39428,
      37.78269,
      -122.39377,
      37.78312,
      -122.3937,
      37.78317,
      -122.393,
      37.78363,
      -122.39294,
      37.78358,
      -122.39258,
      37.78384,
      -122.39234,
      37.78402,
      -122.39231,
      37.78405,
      -122.39227,
      37.78408,
      -122.39222,
      37.78411,
      -122.39214,
      37.78417,
      -122.39207,
      37.78422,
      -122.39144,
      37.78471,
      -122.39122,
      37.78492,
      -122.39094,
      37.78522,
      -122.39087,
      37.78529,
      -122.39081,
      37.78534,
      -122.39003,
      37.78598,
      -122.3897,
      37.78621,
      -122.38963,
      37.78625,
      -122.38955,
      37.78629,
      -122.38904,
      37.78667,
      -122.38875,
      37.78691,
      -122.38872,
      37.78693,
      -122.38878,
      37.78698,
      -122.38867,
      37.78705,
      -122.3886,
      37.78709,
      -122.38857,
      37.7871,
      -122.38855,
      37.78711,
      -122.38852,
      37.78712,
      -122.38849,
      37.78713,
      -122.38846,
      37.78713,
      -122.38843,
      37.78714,
      -122.38835,
      37.78715,
      -122.38819,
      37.78715,
      -122.38816,
      37.78715,
      -122.38806,
      37.78714
    ]

    github_data_4 = \
    [
        -122.39348,
        37.78079,
        -122.39328,
        37.78096,
        -122.39321,
        37.78101,
        -122.39266,
        37.78146,
        -122.39215,
        37.78186,
        -122.39209,
        37.78191,
        -122.39134,
        37.78251,
        -122.39066,
        37.78305,
        -122.38992,
        37.78363,
        -122.38986,
        37.78357,
        -122.3906,
        37.783,
        -122.39124,
        37.78249,
        -122.38981,
        37.78135,
        -122.38976,
        37.7813,
        -122.38982,
        37.78125,
        -122.38987,
        37.7813,
        -122.38981,
        37.78135,
        -122.38976,
        37.7813,
        -122.3896,
        37.78143,
        -122.38956,
        37.78146,
        -122.38937,
        37.7816,
        -122.38935,
        37.78162,
        -122.3893,
        37.78165,
        -122.38923,
        37.7817,
        -122.38919,
        37.78172,
        -122.38915,
        37.78173,
        -122.38912,
        37.78175,
        -122.38903,
        37.78178,
        -122.38896,
        37.78179,
        -122.3889,
        37.78181,
        -122.38883,
        37.78182,
        -122.38876,
        37.78183,
        -122.38871,
        37.78184,
        -122.38866,
        37.78184,
        -122.38861,
        37.78185,
        -122.38856,
        37.78185,
        -122.38847,
        37.78185,
        -122.38838,
        37.78184,
        -122.3882,
        37.78183,
        -122.38811,
        37.78183,
        -122.38811,
        37.78178,
        -122.38805,
        37.78177,
        -122.38802,
        37.78214,
        -122.38801,
        37.78252,
        -122.38793,
        37.78324,
        -122.38792,
        37.78339,
        -122.38792,
        37.78347,
        -122.3879,
        37.78365,
        -122.38781,
        37.78463,
        -122.3878,
        37.78474,
        -122.38766,
        37.78474,
        -122.38766,
        37.78468,
        -122.38765,
        37.78466,
        -122.38765,
        37.78465,
        -122.38764,
        37.78464,
        -122.38762,
        37.78463,
        -122.38761,
        37.78463,
        -122.3876,
        37.78462,
        -122.3876,
        37.78461,
        -122.38759,
        37.78457,
        -122.38758,
        37.78455,
        -122.38758,
        37.7845,
        -122.38754,
        37.78414,
        -122.38752,
        37.78394,
        -122.38752,
        37.78392,
        -122.38752,
        37.7839,
        -122.38753,
        37.78388,
        -122.38754,
        37.78386,
        -122.38754,
        37.78384,
        -122.38754,
        37.78382,
        -122.38755,
        37.7838,
        -122.38755,
        37.78379,
        -122.38755,
        37.7837,
        -122.38755,
        37.78367,
        -122.38755,
        37.78366,
        -122.38755,
        37.78364,
        -122.38756,
        37.7836,
        -122.38756,
        37.78359,
        -122.38756,
        37.78358,
        -122.38757,
        37.78357,
        -122.38757,
        37.78355,
        -122.38758,
        37.78354,
        -122.38759,
        37.78353,
        -122.38761,
        37.7835,
        -122.38763,
        37.78348,
        -122.38764,
        37.78347,
        -122.38765,
        37.78346,
        -122.38768,
        37.78345,
        -122.38771,
        37.78345,
        -122.38773,
        37.78345,
        -122.38779,
        37.78345,
        -122.38782,
        37.78346,
        -122.38786,
        37.78347,
        -122.38792,
        37.78347,
        -122.3879,
        37.78365,
        -122.38789,
        37.78374
    ]

    github_data_5 = \
    [
        -122.39274,
        37.78244,
        -122.39282,
        37.7825,
        -122.39303,
        37.78267,
        -122.3931,
        37.78272,
        -122.39332,
        37.78286,
        -122.39364,
        37.78312,
        -122.3937,
        37.78317,
        -122.39377,
        37.78312,
        -122.39428,
        37.78269,
        -122.3948,
        37.78225,
        -122.39585,
        37.7814,
        -122.39579,
        37.78135,
        -122.39587,
        37.78128,
        -122.39558,
        37.78105,
        -122.39524,
        37.78078,
        -122.39512,
        37.78069,
        -122.39468,
        37.78032,
        -122.39439,
        37.7801,
        -122.39431,
        37.78017,
        -122.39457,
        37.78036,
        -122.39463,
        37.78041,
        -122.39501,
        37.78073,
        -122.39466,
        37.78101,
        -122.39463,
        37.78108,
        -122.39465,
        37.78112,
        -122.39465,
        37.78116,
        -122.39464,
        37.78119,
        -122.39462,
        37.78123,
        -122.39459,
        37.78126,
        -122.39408,
        37.78167,
        -122.39356,
        37.78208,
        -122.39353,
        37.7821,
        -122.39348,
        37.78211,
        -122.39344,
        37.78212,
        -122.3934,
        37.78212,
        -122.39336,
        37.78211,
        -122.39332,
        37.78209,
        -122.39322,
        37.78212,
        -122.3932,
        37.78206,
        -122.39319,
        37.78202,
        -122.3932,
        37.78199,
        -122.39321,
        37.78196,
        -122.39323,
        37.78191,
        -122.39326,
        37.78186,
        -122.39378,
        37.78148,
        -122.39351,
        37.78125,
        -122.39321,
        37.78101,
        -122.39328,
        37.78096,
        -122.39354,
        37.78117,
        -122.39361,
        37.78123,
        -122.39385,
        37.78143,
        -122.39392,
        37.78149,
        -122.39394,
        37.78149,
        -122.39398,
        37.78152,
        -122.39408,
        37.78161,
        -122.3941,
        37.78165,
        -122.39411,
        37.78164,
        -122.39418,
        37.78169,
        -122.39444,
        37.7819,
        -122.3945,
        37.78195,
        -122.39477,
        37.78217,
        -122.39483,
        37.78222,
        -122.3948,
        37.78225,
        -122.39428,
        37.78269,
        -122.39377,
        37.78312,
        -122.3937,
        37.78317,
        -122.39414,
        37.78355,
        -122.39417,
        37.78357
    ]

    populate_multiple(github_data_1, 1, my_db, my_cursor)
    populate_multiple(github_data_2, 2, my_db, my_cursor)
    populate_multiple(github_data_3, 3, my_db, my_cursor)
    populate_multiple(github_data_4, 4, my_db, my_cursor)
    populate_multiple(github_data_5, 5, my_db, my_cursor)


def populate_multiple(github_data, client_id, my_db, my_cursor):
    latitude = None
    longitude = None
    unix_time = 0

    la = []
    lo = []

    for index, elem in enumerate(github_data):
        if index % 2 == 0:
            la.append(elem)
        else:
            lo.append(elem)

    for index, elem in enumerate(la):
        add_interceptor_command = "INSERT INTO geodata (client_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s)"
        add_interceptor_command_variables = (client_id, lo[index], elem, unix_time)
        my_cursor.execute(add_interceptor_command, add_interceptor_command_variables)
        my_db.commit()
        unix_time += 1

# ---------------------------------------------------------intercepts---------------------------------------------------------------------
    latitude_list = [30.3358376, 30.307977, 30.3216419]
    longitude_list = [77.8701919, 78.048457, 78.0413095]
    interceptor_ids = [987654321, 908765432, 876543210]

    for index, elem in enumerate(latitude_list):
        add_interceptor_command = "INSERT INTO intercepts (client_id, interceptor_id, latitude, longitude, unix_time) VALUES (%s, %s, %s, %s, %s)"
        add_interceptor_command_variables = (client_id, interceptor_ids[index], elem, longitude_list[index], unix_time)
        my_cursor.execute(add_interceptor_command, add_interceptor_command_variables)
        my_db.commit()
        unix_time += 1


if __name__ == '__main__':
    main()
