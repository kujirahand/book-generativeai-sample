import os

def split_file(input_file, output_file_prefix, chunk_size):
    file_size = os.path.getsize(input_file)
    n_chunks = -(-file_size // chunk_size)  # Ceiling division

    with open(input_file, 'rb') as f:
        for i in range(n_chunks):
            chunk = f.read(chunk_size)
            with open(f'{output_file_prefix}_{i:03d}', 'wb') as chunk_file:
                chunk_file.write(chunk)


if __name__ == '__main__':
    input_file = 'example.mp4'  # 分割したいファイル名を指定
    output_file_prefix = 'example_chunk'  # 分割されたファイルのプレフィックスを指定
    chunk_size = 500 * 1024 * 1024  # 分割サイズ（500MB）

    split_file(input_file, output_file_prefix, chunk_size)
