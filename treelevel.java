package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class treelevel {
	public int maxDepth(Node root) {
	       
        if (root == null) return 0;
        Queue<Node> Q = new LinkedList<Node>(); 
        Q.offer(root);
        int depth = 0;
        
        while (Q.size() > 0){
            int size = Q.size();
            
            for (int i = 0; i < size; i ++){
                Node currentprocess = Q.poll();
                for (Node c:currentprocess.children){
                    Q.offer(c);
                }
            }
       
            depth ++;
        }
        return depth;
    }
}
