from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument('wells', type=int, metavar='Number of wells')
    parser.add_argument('cells', type=float, metavar='Live cell count')
    parser.add_argument('power', nargs='?', default=0, type=int, help='Power of 10 to multiply the cell count by (default 0)', metavar='Cell power')
    parser = parser.parse_args()
    cellVolume = parser.wells * 50000000 * 10 ** -parser.power / parser.cells
    print(f'Add {cellVolume} µl cells to {parser.wells * 80 - cellVolume} µl DMEM')


if __name__ == '__main__':
    main()
