/*--------------------------------------------------------------------
Name: Emmanuel Robles Cruz
Student ID: 1002240139
COP 2805C - Java Programming 2
fall / 2017
Assignment # 2
Plagiarism Statement
I certify that this assignment is my own work and that I have not copied in part or whole or otherwise plagiarized the work of other students and/or persons.
--------------------------------------------------------------------*/
/*
Task:
Perform set operations on hash sets. Create a class named TestHashSetOperations to do the following. Create two linked hash sets 
{"George", "Jim", "John", "Blake", "Kevin", "Michael"} and {"George", "Katie", "Kevin", "Michelle", "Ryan"} and find their union, 
difference, and intersection. (You can clone the sets to preserve the original sets from being changed by these set methods.)
*/
import java.util.*;

public class TestHashSetOperations {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedHashSet<String> set1= new LinkedHashSet<>(Arrays.asList("George", "Jim", "John", "Blake", "Kevin", "Michael"));
		LinkedHashSet<String> set2= new LinkedHashSet<>(Arrays.asList("George", "Katie", "Kevin", "Michelle", "Ryan"));
		
		//System.out.println("Original Set1 before opp:"+set1);
		//System.out.println("Original Set2 before opp:"+set2);

		//union
		LinkedHashSet<String> setUnion=new LinkedHashSet<>(set1);
		setUnion.addAll(set2);
		System.out.println("Union: "+setUnion);
		
		//difference
		LinkedHashSet<String> setDiff=new LinkedHashSet<>(set1);
		setDiff.removeAll(set2);
		System.out.println("Difference S1-S2:"+setDiff);
		
		setDiff=new LinkedHashSet<>(set2);
		setDiff.removeAll(set1);
		System.out.println("Difference S2-S1:"+setDiff);
		
		//intersection
		LinkedHashSet<String> setInter=new LinkedHashSet<>(set1);
		setInter.retainAll(set2);
		System.out.println("Intersection:"+setInter);
		
		//System.out.println("Original Set1 after opp:"+set1);
		//System.out.println("Original Set2 after opp:"+set2);
	}

}
