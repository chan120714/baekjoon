import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a[] = new int[5465];
        int t=0;
        int n = 28;
        for (int i=0;i<n;i++){
            int x=sc.nextInt();
            a[x]+=1;
        }
        for (int i=1;i<=30;i++)if(a[i]==0)System.out.println(i);
    }
}