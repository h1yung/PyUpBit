<!-- Find and Replace All [repo_name] -->
<!-- Replace [product-screenshot] [product-url] -->
<!-- Other Badgets https://naereen.github.io/badges/ -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![License][license-shield]][license-url] -->

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">PyUpBit</h3>

  <p align="center">
    CS490 Large Scale Data Analytics — Implementation of Updatable Compressed Bitmap Indexing
    <br />
    <a href="https://github.com/h1yung/PyUpBit/blob/main/pyupbit_report.pdf">Paper</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
	  <li><a href="#about-the-project">About The Project</a></li>
	  <li><a href="#usage">Usage</a></li>
	  <!-- <li><a href="#license">License</a></li> -->
	  <li><a href="#contact">Contact</a></li>
	  <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Bitmaps are common data structures used in database implemen- tations due to having fast read performance. Often they are used in applications in need of common equality and selective range queries. Essentially, they store a bit-vector for each value in the domain of each attribute to keep track of large scale data files. How- ever, the main drawbacks associated with bitmap indexes are its encoding and decoding performances of bit-vectors.
Currently the state of art update-optimized bitmap index, update conscious bitmaps, are able to support extremely efficient deletes and have improved update speeds by treating updates as delete then insert. Update conscious bitmaps make use of an additional bit-vector, called the existence bit-vector, to keep track of whether or not a value has been updated. By initializing all values of the existence bit-vector to 1, the data for each attribute associated with each row in the existence bit-vector is validated and presented. If a value needs to be deleted, the corresponding row in the existence bit-vector gets changed to 0, invalidating any data associated with that row. This new method in turn allows for very efficient deletes. To add on, updates are then performed as a delete operation, then an insert operation in to the end of the bit-vector.
However, update conscious bitmaps do not scale well with more data. As more and more data gets updated and inserted, the run time increases significantly as well. Because update queries are out-of- place and increase size of vectors, read queries become increasingly expensive and time consuming. Furthermore, as the number of updates and deletes increases, the bit-vector becomes less and less compressible.
This brings us to updateable Bitmaps (UpBit). According to the paper, UpBit: Scalable In-Memory Updatable Bitmap Indexing, re- searchers Manos Athanassoulis, Zheng Yan, and Stratos Idreos developed a new bitmap structure that improved the write per- formance of bitmaps without sacrificing read performance. The main differentiating point of UpBit is its use of an update bit vector for every value in the domain of an attribute that keeps track of updated values. This allows for faster write performance without sacrificing read performance.
Based on this paper, we implemented UpBit and compared it to our implementation of update conscious bitmaps to compare and test the performances of both methods.

<!-- USAGE EXAMPLES -->
## Usage

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources. -->

We used PyCharm to conduct our tests, /ucb, /upbit for algorithms, /tests for running testing scripts, and rest of the files for compression for memory usage improvement as well as creating and visualizing data.


<!-- CONTACT -->
## Contact

Daniel Park - [@h1yung][linkedin-url] - h1yungpark@gmail.com

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

- <a href="https://stratos.seas.harvard.edu/publications/upbit-scalable-memory-updatable-bitmap-indexing">Original Paper</a>
- Winston Chen
- Gregory Chininis
- Daniel Hooks
- Michael Lee

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/h1yung/PyUpBit.svg?style=for-the-badge
[contributors-url]: https://github.com/h1yung/PyUpBit/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/h1yung/PyUpBit.svg?style=for-the-badge
[forks-url]: https://github.com/h1yung/PyUpBit/network/members
[stars-shield]: https://img.shields.io/github/stars/h1yung/PyUpBit.svg?style=for-the-badge
[stars-url]: https://github.com/h1yung/PyUpBit/stargazers
[issues-shield]: https://img.shields.io/github/issues/h1yung/PyUpBit.svg?style=for-the-badge
[issues-url]: https://github.com/h1yung/PyUpBit/issues
<!-- [license-shield]: 
[license-url]:  -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/h1yung/


