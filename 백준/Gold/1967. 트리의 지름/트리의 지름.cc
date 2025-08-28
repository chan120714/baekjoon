#include<bits/stdc++.h>
using namespace std;

vector< pair< int , int > > arr[ 10009 ];
int vis_1[ 10009 ], vis_2[ 10009 ];
int s[ 10009 ];
int ss[ 10009 ];

void dfs_1( int v, int sum ){
	vis_1[ v ] = 1;
	for( int i = 0; i < arr[ v ].size(); i ++ )
		if( !vis_1[ arr[ v ][ i ].first ] ){ 
			dfs_1( arr[ v ][ i ].first, sum + arr[ v ][ i ].second );
		}
	s[ v ] = sum;
	return;
}

void dfs_2( int v, int sum ){
	vis_2[ v ] = 1;	
	ss[ v ] = sum;
	for( int i = 0; i < arr[ v ].size(); i ++ ) 
		if( !vis_2[ arr[ v ][ i ].first ] ){ 
			dfs_2( arr[ v ][ i ].first, sum + arr[ v ][ i ].second );
		}
	ss[ v ] = sum;
	return;
}

int main(){
	int n;
	cin >> n;
	for( int i = 1; i < n; i ++ ){
		int st, ed, we;
		cin >> st >> ed >> we;
		arr[ st ].push_back( { ed, we } );
		arr[ ed ].push_back( { st, we } );
	}
	
	dfs_1( 1, 0 );
	int max_v = 0, max_n=1;
	for( int i = 1; i <= n; i ++ ){
		if( s[ i ] > max_v ){
			max_v = s[ i ];
			max_n = i;
		}
	}
	
	dfs_2( max_n, 0 );
	sort( ss+1, ss + n+1 );
	
	
	cout << ss[ n ];
	
	return 0;
}