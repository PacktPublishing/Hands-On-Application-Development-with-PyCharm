if __name__ == '__main__':
    print('You have successfully imported this project.')

    try:
        import tqdm
        print('You also have tqdm!')
    except ModuleNotFoundError:
        print('You do not have tqdm.')
