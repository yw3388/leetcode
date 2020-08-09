/*
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
*/
class union {
	public int[]  parents;
	public int count;
	
	public int union(int length) {
		parents = new int[length];
		for(int i =0; i < length; i++) {
			parents[i] = i;
		}
	}
	public int find(int node) {
		if (node == parents[node]) {
			return node;
		}
		/* recursively find the group to see what group*/
		return parents[node] = find(parents[node]);
	}
	
	public void uniontwo(int a, int b) {
		int g = find(a);
		int f = find(b);
		/*merge two groups together into one*/
		if (g != f) {
			parents[f] = g;
			this.count --;
		}
	}
	public void set(int c) {
		this.count = c;
	}
	
}


public Solution{
	public int findCircleNum(int[][] M) {
		if(M.length == 0|| M[0].length == 0) {
			return 0;
		}
		int m = M.length;
		int n = M[0].length;
		union unit = new union();
		unit.set(m*n);
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if (M[i][j] == 1 & i != j) {
					unit.uniontwo(i, j);
					
				}
			}
		}
		return unit.count;
	}
}