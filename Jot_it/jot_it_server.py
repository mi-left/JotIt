from flask import Flask, request
import threading
import time

operator_addr = ''
endpoints = []
endpoint_dict = {
    "/arrays" : "0",
    "/linked-lists" : "1",
    "/stacks" : "2",
    "/queues" : "3",
    "/hash-tables" : "4",
    "/trees" : "5",
    "/graphs" : "6",
    "/heaps" : "7",
    "/tries" : "8",
    "/graphs-algorithms" : "9",
    "/dynamic-programming" : "a",
    "/sorting-algorithms" : "b",
    "/search-algorithms" : "c",
    "/object-oriented-programming" : "d",
    "/divide-and-conquer" : "e",
    "/greedy-algorithms" : "f",
}

def check_request(request):
    global operator_addr
    global endpoints
    # Access the request cookies
    cookies = request.cookies
    # Get the IP address of the client
    ip_address = request.remote_addr

    if(ip_address == operator_addr):
        endpoints.append(str(request.path))

    if cookies.get("username") == "jamescharles5462456":
        operator_addr = ip_address


def receive_covert_comms():
    count = 0
    binary = ""
    while True:
        f = open("covert_message.txt", "w")
        i = 0
        for endpoint in endpoints:
            i+=1
            if i <= count:
                continue
            else:
                binary = binary + endpoint_dict.get(endpoint)
                count+=1
        if len(binary) % 2 == 0:
            data = bytes.fromhex(binary).decode()
            f.write(data)
            f.close()
        time.sleep(15)

app = Flask(__name__)
@app.route('/arrays', methods=['GET'])
def handle_arrays():
    check_request(request)
    return """

      ____.       __    .__  __   
    |    | _____/  |_  |__|/  |_ 
    |    |/    \   __\ |  \   __|
/\__|    (      )  |   |  ||  |  
\________|\____/|__|   |__||__|  


    Blog Post 1 
    ARRAYS 
                                 
    Arrays are a fundamental data structure in computer science. 
    They are collections of elements, each identified by an index or a key. 
    Arrays offer constant-time access to elements, making them efficient for random access. 
    However, resizing arrays can be costly as it may involve creating a new, larger array and copying elements from the old one."""

@app.route('/linked-lists', methods=['GET'])
def handle_linked_lists():
    check_request(request)
    return """

      ____.       __    .__  __   
    |    | _____/  |_  |__|/  |_ 
    |    |/    \   __\ |  \   __|
/\__|    (      )  |   |  ||  |  
\________|\____/|__|   |__||__|  


    Blog Post 2 
    LINKED LISTS 
                                 
Linked lists are an essential data structure. 
They consist of nodes, where each node holds data and a reference (pointer) to the next node. 
Linked lists provide efficient insertion and deletion operations, especially when modifying elements in the middle. 
However, accessing elements in a linked list is slower compared to arrays, as it requires traversing the list from the beginning."""

@app.route('/stacks', methods=['GET'])
def handle_stacks():
    check_request(request)
    return "Stacks are a data structure that follows the Last-In-First-Out (LIFO) principle. Elements are added and removed from the same end called the top. This makes stacks useful for tasks like expression evaluation, backtracking, and managing function calls. Python lists can be used as a simple implementation of stacks."

@app.route('/queues', methods=['GET'])
def handle_queues():
    check_request(request)
    return "Queues are a data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at the rear and removed from the front. They are useful for tasks like task scheduling, breadth-first search algorithms, and managing resources in computer systems."

@app.route('/hash-tables', methods=['GET'])
def handle_hash_tables():
    check_request(request)
    return "Hash tables (or dictionaries in Python) are a data structure that stores key-value pairs. They use a hash function to map keys to specific locations in the underlying array, enabling fast access to values. Hash tables are efficient for lookups, inserts, and deletions when the hash function distributes the keys uniformly."

@app.route('/trees', methods=['GET'])
def handle_trees():
    check_request(request)
    return "Trees are hierarchical data structures consisting of nodes connected by edges. They have a root node, internal nodes, and leaf nodes. Trees are commonly used in hierarchical representations and for efficient searching and sorting operations. Binary trees, balanced trees like AVL and Red-Black trees, and B-trees are some important variants."

@app.route('/graphs', methods=['GET'])
def handle_graphs():
    check_request(request)
    return "Graphs are versatile data structures composed of vertices (nodes) connected by edges. They are used to model complex relationships and are fundamental in graph algorithms like Dijkstra's algorithm for shortest paths, Kruskal's algorithm for minimum spanning trees, and graph traversals like depth-first search (DFS) and breadth-first search (BFS)."

@app.route('/heaps', methods=['GET'])
def handle_heaps():
    check_request(request)
    return "Heaps are specialized trees that satisfy the heap property. In a min-heap, the parent node's value is smaller than or equal to its children, and in a max-heap, the parent's value is greater. Heaps are commonly used to implement priority queues, which allow efficient access to the minimum or maximum element."

@app.route('/tries', methods=['GET'])
def handle_tries():
    check_request(request)
    return "Tries (also called prefix trees) are tree-like data structures used to efficiently store and search strings. Each node represents a character, and the path from the root to a node forms a string. Tries are useful for tasks like autocomplete suggestions, spell checking, and efficient string searches."

@app.route('/graphs-algorithms', methods=['GET'])
def handle_graph_algorithms():
    check_request(request)
    return "Graph algorithms play a crucial role in computer science. They help solve various real-world problems, including finding the shortest path, detecting cycles, and identifying connected components in graphs. Algorithms like Dijkstra's, Kruskal's, DFS, and BFS are essential tools for analyzing and manipulating graph structures."

@app.route('/dynamic-programming', methods=['GET'])
def handle_dynamic_programming():
    check_request(request)
    return "Dynamic programming is a powerful technique used to solve complex problems by breaking them into overlapping subproblems and reusing their solutions. It's commonly applied to optimize recursive algorithms and efficiently solve problems like the knapsack problem, Fibonacci sequence, and finding the longest common subsequence."

@app.route('/sorting-algorithms', methods=['GET'])
def handle_sorting_algorithms():
    check_request(request)
    return "Sorting algorithms are essential for organizing data efficiently. Various algorithms like bubble sort, selection sort, merge sort, quicksort, and radix sort offer different trade-offs in terms of time complexity and stability. Choosing the right sorting algorithm is crucial for optimizing performance in different scenarios."

@app.route('/search-algorithms', methods=['GET'])
def handle_search_algorithms():
    check_request(request)
    return "Search algorithms help find specific elements in data structures efficiently. Popular algorithms include linear search, binary search, depth-first search (DFS), and breadth-first search (BFS). Each algorithm has its strengths and weaknesses, making them suitable for different search scenarios."

@app.route('/algorithm-complexity', methods=['GET'])
def handle_algorithm_complexity():
    check_request(request)
    return "Understanding algorithm complexity is essential for evaluating the efficiency of algorithms. Big O notation is commonly used to describe the worst-case time complexity of an algorithm. Analyzing complexity helps identify bottlenecks and select the most suitable algorithm for specific problem sizes."

@app.route('/object-oriented-programming', methods=['GET'])
def handle_oop():
    check_request(request)
    return "Object-Oriented Programming (OOP) is a popular programming paradigm that emphasizes organizing code around objects and classes. OOP concepts, such as inheritance, encapsulation, and polymorphism, facilitate code reusability, maintainability, and modularity. Python, Java, and C++ are some common languages that support OOP."

@app.route('/recursion', methods=['GET'])
def handle_recursion():
    check_request(request)
    return "Recursion is a powerful programming technique where a function calls itself to solve a problem. It's commonly used in algorithms like factorials, Fibonacci sequence, and traversing complex data structures like trees and graphs. While elegant, improper use of recursion can lead to stack overflow errors."

@app.route('/divide-and-conquer', methods=['GET'])
def handle_divide_and_conquer():
    check_request(request)
    return "Divide and Conquer is a problem-solving paradigm that breaks a problem into smaller subproblems, solves them independently, and combines their solutions to find the final answer. This approach is commonly used in algorithms like merge sort, quicksort, and binary search, achieving efficient solutions for various problems."

@app.route('/greedy-algorithms', methods=['GET'])
def handle_greedy_algorithms():
    check_request(request)
    return "Greedy algorithms make locally optimal choices at each step to find the global optimum. While not always providing the best result, they are easy to implement and can be highly efficient. Common examples include the coin change problem, the knapsack problem, and the minimum spanning tree algorithm."

@app.route('/backtracking', methods=['GET'])
def handle_backtracking():
    return "Backtracking is a technique used to systematically explore all possible solutions to a problem by trying out various choices and undoing them when necessary. It's commonly used in problems like the N-Queens problem, Sudoku, and solving puzzles with multiple solutions."

@app.route('/bit-manipulation', methods=['GET'])
def handle_bit_manipulation():
    return "Bit manipulation involves manipulating individual bits of data to achieve specific operations efficiently. It's often used in optimizing code, setting or clearing flags, and solving problems like finding unique elements in an array or representing sets using bit masks."

@app.route('/dynamic-memory-allocation', methods=['GET'])
def handle_dynamic_memory_allocation():
    return "Dynamic memory allocation allows programs to request memory at runtime, enabling flexible data structures like linked lists and dynamic arrays. However, improper memory management can lead to memory leaks and other issues, making it crucial to deallocate memory when no longer needed."

@app.route('/machine-learning', methods=['GET'])
def handle_machine_learning():
    return "Machine learning is a subset of artificial intelligence that involves building models and algorithms capable of learning from data and making predictions or decisions. Supervised, unsupervised, and reinforcement learning are some common machine learning paradigms used in various applications like image recognition, natural language processing, and recommendation systems."

@app.route('/neural-networks', methods=['GET'])
def handle_neural_networks():
    return "Neural networks are a class of machine learning models inspired by the human brain's structure. They consist of interconnected nodes (neurons) organized into layers. Neural networks are widely used in deep learning and are responsible for significant advancements in tasks like image recognition, natural language processing, and game playing."

@app.route('/database-management', methods=['GET'])
def handle_database_management():
    return "Database management systems (DBMS) are software that facilitates storing, organizing, and retrieving data efficiently. Common types include relational databases (SQL), NoSQL databases (e.g., MongoDB, Redis), and graph databases. Understanding database design and query optimization is essential for building scalable and performant applications."

def main():
    f = open("covert_message.txt", "w")
    f.write("")
    f.close()    
    thread = threading.Thread(target=receive_covert_comms)
    thread.start()
