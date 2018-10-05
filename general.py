import os

# Each website you crawl is a seperate folder
def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    create_dir(project_name)
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


#create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

create_data_files('code', 'https://www.codechef.com/')

#Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#delete the contents of a filr
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set, each item will be a new linr in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)