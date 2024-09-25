from mrjob.job import MRJob

class MRWordCount(MRJob):
    
    def mapper(self, _, line):
        # Mapper: Tách từng từ trong dòng và trả về mỗi từ với giá trị 1
        for word in line.split():
            yield word.lower(), 1
    
    def reducer(self, key, values):
        # Reducer: Cộng tổng số lần xuất hiện của mỗi từ
        yield key, sum(values)

if __name__ == '__main__':
    MRWordCount.run()
