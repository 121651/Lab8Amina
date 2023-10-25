class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.process = None

def best_fit(memory, process):
    best_fit_block = None

    for block in memory:
        if block.size >= process['size'] and (best_fit_block is None or block.size < best_fit_block.size):
            best_fit_block = block

    if best_fit_block:
        best_fit_block.process = process
        return True
    else:
        return False

def first_fit(memory, process):
    for block in memory:
        if block.size >= process['size']:
            block.process = process
            return True

    return False
