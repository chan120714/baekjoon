import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a[] = new int[5465];
        int t=0;
        int n = sc.nextInt();
        for (int i=0;i<n;i++){
            int x=sc.nextInt();
            a[x+100]+=1;
        }
        int x=sc.nextInt();
        System.out.println(a[x+100]);
    }
}