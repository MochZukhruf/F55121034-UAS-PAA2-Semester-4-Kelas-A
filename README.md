# F55121034-Moch.Zukhruf-Ain-UAS-PAA2-Semester-4-Kelas-A

Nama : Moch. Zukhruf Ain

NIM : F55121034

Kelas A 

No. 1
- Analisis Algoritma Bubble Sort 
Algoritma Bubble Sort memiliki kompleksitas waktu rata-rata O(n^2), di mana n adalah jumlah elemen dalam array. Pada setiap iterasi, algoritma melakukan perbandingan dan penukaran pada elemen-elemen adjacent. Jika array terurut secara terbalik, maka algoritma akan memerlukan n iterasi untuk mengurutkan array tersebut. Pada kasus terbaik, di mana array sudah terurut secara ascending, algoritma akan memiliki kompleksitas waktu O(n), namun pada umumnya kompleksitasnya O(n^2), algoritma ini memiliki kelebihan yaitu implementasi yang sederhana dan mudah dipahami dan Cocok digunakan pada kasus-kasus di mana jumlah elemen yang diurutkan relatif kecil namun juga memiliki kekurangan yaitu memiliki performa yang relatif buruk dibandingkan dengan algoritma pengurutan lainnya, terutama pada kasus-kasus dengan jumlah elemen yang besar. Algoritma ini cenderung lambat karena memerlukan banyak iterasi dan pertukaran elemen.
1. Worst Case 
Worst case terjadi ketika array dalam keadaan terbalik secara terurut. Misalnya, jika array yang diberikan sudah dalam keadaan terurut secara menurun, Bubble Sort akan melakukan penukaran elemen pada setiap iterasi di dalam nested loop. Dalam hal ini, kompleksitas waktu Bubble Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
2. Best Case
Best case terjadi ketika array sudah dalam keadaan terurut secara menaik. Dalam hal ini, Bubble Sort akan melewati iterasi kedua dalam nested loop tanpa melakukan penukaran apapun. Kompleksitas waktu Bubble Sort pada best case adalah O(n), di mana n adalah jumlah elemen dalam array.
3. Average Case
Average case dari Bubble Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array. Ini terjadi karena dalam kasus rata-rata, Bubble Sort akan melakukan beberapa penukaran elemen pada setiap iterasi di dalam nested loop.

Analisis Algoritma Insertion Sort
Insertion Sort adalah algoritma pengurutan yang bekerja dengan membagi array menjadi dua bagian: bagian terurut dan bagian belum terurut. Pada setiap iterasi, algoritma memilih elemen dari bagian belum terurut dan memasukkannya ke tempat yang tepat dalam bagian terurut algoritma ini memiliki kelebihan implementasi yang sederhana dan mudah dipahami. Lebih cepat daripada Bubble Sort dalam beberapa kasus tergantung pada data yang diurutkan. Cocok digunakan pada kasus-kasus di mana jumlah elemen yang diurutkan relatif kecil atau array sudah hampir terurut dan juga kekurangan yaitu memiliki performa yang buruk pada kasus-kasus dengan jumlah elemen yang besar. Algoritma ini memerlukan banyak perpindahan elemen saat memasukkan elemen ke dalam bagian terurut.
1. Worst Case 
Worst case terjadi ketika array dalam keadaan terbalik secara terurut, seperti pada Bubble Sort. Dalam hal ini, kompleksitas waktu Insertion Sort juga adalah O(n^2), di mana n adalah jumlah elemen dalam array.
2. Best Case
Best case terjadi ketika array sudah dalam keadaan terurut secara menaik. Dalam hal ini, Insertion Sort hanya perlu membandingkan setiap elemen dengan elemen sebelumnya tanpa perlu melakukan penukaran. Kompleksitas waktu Insertion Sort pada best case adalah O(n), di mana n adalah jumlah elemen dalam array.
3. Average Case
Average case dari Insertion Sort juga adalah O(n^2), di mana n adalah jumlah elemen dalam array. Hal ini terjadi karena dalam kasus rata-rata, Insertion Sort akan melakukan beberapa pergeseran elemen pada setiap iterasi while loop di dalam for loop.
- Jadi dapat disimpulkan bahwa algoritma bubble sort dan insertion sort dimana insertion Sort memiliki kompleksitas waktu terbaik (best case) O(n), ketika array yang diurutkan sudah dalam keadaan terurut secara menaik. Namun, kompleksitas waktu terburuk (worst case) dan rata-rata (average case) Insertion Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array dan juga Bubble Sort memiliki kompleksitas waktu terbaik (best case), terburuk (worst case), dan rata-rata (average case) yang sama, yaitu O(n^2), di mana n adalah jumlah elemen dalam array, Kedua algoritma, Insertion Sort dan Bubble Sort, tidak memerlukan ruang tambahan yang besar dan dapat diimplementasikan dengan menggunakan ruang konstan (O(1)) namun juga dapat diingat jika ingin mengurutkan array dengan jumlah elemen yang besar, ada algoritma pengurutan lain yang lebih efisien, seperti Merge Sort atau Quick Sort.

No.2
Analisis Algoritma TSP dan Dijkstra
TSP (Traveling Salesman Problem) dan Dijkstra adalah dua masalah terkenal dalam teori graf yang memerlukan pendekatan algoritma yang berbeda. TSP adalah masalah optimisasi yang bertujuan mencari jalur terpendek yang mengunjungi semua titik dalam graf yang terhubung, sedangkan Dijkstra adalah algoritma yang digunakan untuk mencari jalur terpendek antara dua titik dalam graf berbobot.
kemudian dapat diketahui bahwa Analisis TSP (Traveling Salesman Problem):
- TSP adalah masalah NP-sulit, yang berarti tidak ada algoritma efisien yang dapat menyelesaikan TSP pada semua kasus dalam waktu yang wajar. Oleh karena itu, solusi TSP seringkali melibatkan pendekatan heuristik dan algoritma aproksimasi.
- TSP mencari jalur terpendek yang melewati semua titik dengan kembali ke titik awal. Dalam kasus yang lebih umum, graf yang diberikan tidak memiliki sifat khusus seperti jarak yang simetris atau mematuhi ketidaksetaraan segitiga.
- Berbagai pendekatan heuristik digunakan untuk menyelesaikan TSP, seperti algoritma Nearest Neighbor, 2-Opt, 3-Opt, Lin-Kernighan, dan algoritma genetika.
analisis worst case, best case dan average case:
- Worst Case: Dalam TSP, tidak ada solusi algoritma yang diketahui untuk memberikan solusi optimal dalam waktu yang terbatas pada semua kasus. Jadi, dalam hal ini, tidak ada perbedaan antara worst case, best case, dan average case. Karena masalah TSP adalah NP-sulit, waktu yang dibutuhkan untuk menyelesaikan masalah secara eksak akan meningkat secara eksponensial dengan jumlah titik yang dikunjungi.
- Best Case: Dalam konteks TSP, tidak ada perbedaan signifikan antara best case dan average case, karena tidak ada algoritma efisien yang diketahui untuk memberikan solusi optimal dalam waktu yang terbatas.
- Average Case: Dalam hal algoritma TSP, tidak ada perbedaan yang signifikan antara average case dan worst case. Karena masalah ini sangat sulit dipecahkan secara eksak pada semua kasus, kinerja algoritma pada kasus-kasus rata-rata juga tidak akan berbeda secara signifikan.
  
Dan juga dapat diketahui bahwa Analisis Dijkstra :
- Dijkstra adalah algoritma pencarian jalur terpendek dalam graf berbobot, di mana bobotnya adalah nilai numerik yang terkait dengan setiap edge dalam graf.
- Algoritma Dijkstra menggunakan pendekatan greedy, mengunjungi simpul-simpul secara berurutan berdasarkan jarak terpendek yang diketahui saat ini.
- Kompleksitas waktu algoritma Dijkstra tergantung pada representasi graf yang digunakan. Dalam representasi matriks ketetanggaan, kompleksitas waktu adalah O(V^2), di mana V adalah jumlah simpul dalam graf. Namun, dengan menggunakan representasi daftar ketetanggaan dan menggunakan struktur data heap, kompleksitas waktu dapat dioptimalkan menjadi O((V + E) log V), di mana E adalah jumlah edge dalam graf.
analisis worst case, best case dan average case:
- Worst Case: Worst case pada algoritma Dijkstra terjadi ketika ada simpul yang sangat jauh dari simpul awal dan diperlukan untuk menjelajahi semua simpul dalam graf. Jika setiap simpul harus dikunjungi dan diperiksa, maka kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah simpul dan E adalah jumlah edge dalam graf.
- Best Case: Best case pada algoritma Dijkstra terjadi ketika simpul tujuan terletak sangat dekat dengan simpul awal, sehingga tidak perlu menjelajahi banyak simpul. Dalam kasus terbaik ini, kompleksitas waktu dapat menjadi lebih rendah dari O((V + E) log V), tergantung pada struktur graf dan implementasi algoritma.
- Average Case: Average case pada algoritma Dijkstra tergantung pada struktur dan karakteristik graf yang diberikan. Jika graf memiliki sifat tertentu, seperti bobot yang seragam atau graf yang sangat terhubung, maka kinerja algoritma dapat meningkat secara signifikan. Namun, pada umumnya, kompleksitas waktu rata-rata algoritma Dijkstra adalah O((V + E) log V), yang merupakan hasil dari menjelajahi sebagian besar simpul dan edge dalam graf.
= Jadi dapat disimpulkan bahwa TSP (Traveling Salesman Problem) adalah masalah optimisasi yang sulit dan NP-sulit. Tidak ada algoritma efisien yang dapat menyelesaikan TSP pada semua kasus dalam waktu yang wajar. Oleh karena itu, solusi TSP sering melibatkan pendekatan heuristik dan algoritma aproksimasi untuk mencapai solusi yang memadai dalam waktu yang terbatas.TSP mencari jalur terpendek yang mengunjungi semua titik dalam graf yang terhubung, dengan kembali ke titik awal. Dalam kasus yang lebih umum, graf yang diberikan tidak memiliki sifat khusus seperti jarak yang simetris atau mematuhi ketidaksetaraan segitiga. Adapun Dijkstra adalah algoritma pencarian jalur terpendek dalam graf berbobot. Algoritma Dijkstra menggunakan pendekatan greedy, mengunjungi simpul-simpul secara berurutan berdasarkan jarak terpendek yang diketahui saat ini. Algoritma Dijkstra bekerja dengan baik pada graf yang tidak memiliki edge dengan bobot negatif. Jika graf memiliki edge dengan bobot negatif, algoritma Bellman-Ford atau algoritma Johnson lebih cocok untuk mencari jalur terpendek.
