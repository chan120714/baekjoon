#include<stdio.h>
int dx[4]={1,-2,1,0},dy[4]={0,0,1,-2},x[1000000],y[1000000],n,m,k,i,j,time[1000000];
int fx,fy,*tx,*ty,t;
main(){
	tx=x;
	ty=y;
	scanf("%d %d",&n,&m);
	int gr[m][n];
	for (i=0;i<m;i++){
		for (j=0;j<n;j++){
			scanf("%d",&gr[i][j]);
			if (gr[i][j]==1){
				x[k]=i+1;y[k]=j+1;
				time[k]=1;
				k+=1;
			}
		}
	}
	for (t=0;t<n*m;t++){
		if (t>k){
			break;
		}
		if (x[t]==0 && y[t]==0){
			continue;
		}
		fx=*(tx+t)-1;fy=*(ty+t)-1;
		for (i=0;i<4;i++){
			fx+=dx[i];fy+=dy[i];
			if (fx<0 || fx>=m || fy<0 || fy>=n){
				continue;
			}
			else{
				if (gr[fx][fy]==0){
					gr[fx][fy]=time[t]+1;
					x[k]=fx+1;y[k]=fy+1;time[k]=time[t]+1;
					k+=1;
				}
				else{
				}
			}
		}
	}
	int max=1;
	for (int i=0;i<m;i++){
		for (int j=0;j<n;j++){
			if (gr[i][j]==0){
				max=2147483647;
			}
			if (gr[i][j]>max){
				max=gr[i][j];
			}
		}
	}
	if (max<1000000){
		printf("%d",max-1);
	}
	else{
		printf("-1");
	}
}