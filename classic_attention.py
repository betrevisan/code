from data import attention_data

TRAIN_SIZE = 100
TEST_SIZE = 30
WIDTH = HEIGHT = 100

def main():
    dataset = attention_data.AttentionData(TRAIN_SIZE, TEST_SIZE, WIDTH, HEIGHT)

if __name__ == "__main__":
    main()