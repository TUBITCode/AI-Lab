# AI-Lab
BIT 4th Semester Artificial Intelligence Practical Lab Assignments

## Artificial Intelligence
### Lab Assignment (FOPL and Prolog)
  1. Consider the following knowledge base and find what would be the output:
      parent(pam,bob).  
      parent(tom,bob).  
      parent(tom,liz).  
      parent(bob,ann).  
      parent(bob,pat).  
      parent(pat,jim).  
    a. ?- parent(bob,pat).  
    b. ?- parent(liz,pat).  
    c. ?-parent(tom,ben).  
    d. ?- parent(X,liz).  
    e. ?- parent(bob,X).  
    f. ?- parent(X,Y).  
    g. Who is a parent of ann? Assume that this is some Y.  
    h. Who is a parent of Y? Assume that this is some X.  
    a. ?- parent(Y,ann), parent(X,Y).  
  2. Given the database below, will the following queries succeed?  
    likes(ram,sita).  
    likes(ram,trains).  
    likes(suresh,fast_cars). 
    likes(Person1,Person2):-  
    hobby(Person1,Hobby),   
    hobby(Person2,Hobby).  
    hobby(ram,trainspotting).   
    hobby(saroj,sailing).   
    hobby(tina,trainspotting).   
    hobby(prakash,sailing).   
    a. likes (ram,trains).  
    b. likes(tina,ram).  
  3. Find the HCF and LCM of any two numbers.  
  4. Write a program to find the factorial of any given number.  
  5. Write a program to find the Fibonacci series.  
  6. Write a program to find the cube of any given number.  
  7. Write a program to calculate the sum, difference, product and division of any two numbers (use read and write predicate).  
  8. Write a program to solve 8-queen problem.  
  9. Horses, cows, pigs are mammals. An offspring of a horse is a horse. Bluebeard is a horse. Bluebeard is Charlie’s parent. Offspring and parent are inverse relations. Every mammal has a parent.   
QUERY: Is Charlie a horse?   
  10. Every American who sells weapons to hostile nations is a criminal. Every enemy of America is a hostile. Iraq has some missiles. All missiles of Iraq were sold by George. George is an American. Iraq is a country. Iraq is the enemy of America. Missiles are weapons.     
QUERY: Is George a criminal?   
  11. All pompeians are romans. All romans were either loyal to Caesar or hated him. Everyone is loyal to someone. People only try to assassinate rulers they are not loyal to. Marcus tried to assassinate Caesar. Marcus was Pompeian.   
QUERY : did marcus hate Caesar?   	
  12. All greedy leaders are autocrat. Autocrats are evils. Shyam is greedy leader. Gopal is a honest leader.  
QUERY: Shyam is evil.  
  13. All people who are graduating are happy. Happy people smiles. Rinku is graduating.  
QUERY: Is Rinku smiles.  
  14. Puppy is dog. All dogs are animals. All animals will die.  
QUERY: Does Puppy die.  
  15. All over smart persons are stupid. Children’s of all stupid persons are naughty. Ram is the children of Hari. Hari is oversmart.  
QUERY:  Does Ram is naughty.  

### Lab Assignment (Searching)
Note: use programming language as C or Python.  
1. Write a program to implement BFS.  
2. Write a program to implement DFS.  
3. Write a program to implement A* search.  

### Lab Assignment (Machine Learning)
Note: use programming language as Python.  
1. Write a program to implement Naïve Bayes algorithm.  
2. Implement the back propagation algorithm.  
3. Write a program to implement genetic algorithm.  

### Lab Assignment (NLP )
Note: use programming language as Python.  
1. Write a program to implement the concept of stemming.  
2. Write a program to implement the concept of lemmatization.  
3. Write a program to implement the concept of part of speech tag (POS).  
4. Write a program to implement the concept of tokenization.  
