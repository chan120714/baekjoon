#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MAX=1500000;
const ll VAL=1234567891234567890;
struct node{
    ll maxv,maxc,smax,minv,minc,smin;
};
node tree[MAX];
ll treeb[MAX],sum_temp[MAX],min_temp[MAX*3],max_temp[MAX*3];
ll temp[MAX],a[MAX>>1];
node merge(node a,node b){// 그냥 case work
    if (a.maxv==b.maxv){
        if (a.minv==b.minv) return {a.maxv,a.maxc+b.maxc,max(a.smax,b.smax),a.minv,a.minc+b.minc,min(a.smin,b.smin)};
        else if (a.minv<b.minv) return {a.maxv,a.maxc+b.maxc,max(a.smax,b.smax),a.minv,a.minc,min(a.smin,b.minv)};
        else return {a.maxv,a.maxc+b.maxc,max(a.smax,b.smax),b.minv,b.minc,min(a.minv,b.smin)};
    }
    if (a.maxv<b.maxv){
        if (a.minv==b.minv) return {b.maxv,b.maxc,max(a.maxv,b.smax),a.minv,a.minc+b.minc,min(a.smin,b.smin)};
        else if (a.minv<b.minv) return {b.maxv,b.maxc,max(a.maxv,b.smax),a.minv,a.minc,min(a.smin,b.minv)};
        else return {b.maxv,b.maxc,max(a.maxv,b.smax),b.minv,b.minc,min(a.minv,b.smin)};
    }
    if (a.minv==b.minv) return {a.maxv,a.maxc,max(a.smax,b.maxv),a.minv,a.minc+b.minc,min(a.smin,b.smin)};
    else if (a.minv<b.minv) return {a.maxv,a.maxc,max(a.smax,b.maxv),a.minv,a.minc,min(a.smin,b.minv)};
    else return {a.maxv,a.maxc,max(a.smax,b.maxv),b.minv,b.minc,min(a.minv,b.smin)};
}
node init(ll n,ll s,ll e){//처음 생성 여기까진 문제없음 
    if (s==e) return tree[n]={a[s],1,-VAL,a[s],1,VAL};
    ll m=(s+e)/2;
    return tree[n]=merge(init(n*2,s,m),init(n*2+1,m+1,e));
}
void sum_lazy(ll n,ll s,ll e){//1번 쿼리 레이지 17476참고 
	if (temp[n]==0) return;
	tree[n].maxv+=temp[n];
	tree[n].minv+=temp[n];
	if (tree[n].smax!=-VAL) tree[n].smax+=temp[n];
	if (tree[n].smin!=VAL) tree[n].smin+=temp[n];
    if (s!=e){
    	for (ll m=n*2;m<=n*2+1;m++){
    		temp[m]+=temp[n];
		}
    }
    // 증명상 문제없음 
    temp[n]=0;
    return;
}
void b_lazy(ll n,ll s,ll e){//1번 쿼리에 대한 B의 변화량 
	if (sum_temp[n]==0) return;
	treeb[n]+=sum_temp[n]*(0ll+e-s+1);
	if (s!=e){
    	sum_temp[n*2]+=sum_temp[n];
    	sum_temp[n*2+1]+=sum_temp[n];
	}
	sum_temp[n]=0;
	return;
}
void min_lazy(ll n,ll s,ll e){ //3번 쿼리 레이지
    if (s==e || min_temp[n]==0) return;
    for (ll m=n*2;m<=n*2+1;m++){
        if (tree[n].maxv<tree[m].maxv){
            if (tree[m].minv==tree[m].maxv) tree[m].minv=tree[n].maxv;
            else if (tree[m].smin==tree[m].maxv) tree[m].smin=tree[n].maxv;
            tree[m].maxv=tree[n].maxv;
        }
	}
}
void max_lazy(ll n,ll s,ll e){ //2번 쿼리 레이지 
    if (s==e || max_temp[n]==0) return;
    for (ll m=n*2;m<=n*2+1;m++){
        if (tree[n].minv>tree[m].minv){
            if (tree[m].maxv==tree[m].minv) tree[m].maxv=tree[n].minv;
            else if (tree[m].smax==tree[m].minv) tree[m].smax=tree[n].minv;
            tree[m].minv=tree[n].minv;
        }
    }
}
void b_maxlazy(ll n, ll s,ll e){
	if (max_temp[n]==0) return;
	treeb[n]+=max_temp[n]*tree[n].minc;
	if (s!=e){
		if (tree[n].minv==tree[n*2].minv) max_temp[n*2]+=max_temp[n];
		if (tree[n].minv==tree[n*2+1].minv) max_temp[n*2+1]+=max_temp[n];
	}
	max_temp[n]=0;
	return;
}
void b_minlazy(ll n, ll s,ll e){
	if (min_temp[n]==0) return;
	treeb[n]+=min_temp[n]*tree[n].maxc;
	if (s!=e){
		if (tree[n].maxv==tree[n*2].maxv) min_temp[n*2]+=min_temp[n];
		if (tree[n].maxv==tree[n*2+1].maxv) min_temp[n*2+1]+=min_temp[n];
	}
	min_temp[n]=0;
	return;
}
void lazy(ll n,ll s,ll e){
    sum_lazy(n,s,e);
    if  (s!=e){
    	sum_lazy(n*2,s,(s+e)/2);
    	sum_lazy(n*2+1,(s+e)/2+1,e);
	}
    max_lazy(n,s,e);
    min_lazy(n,s,e);
    b_lazy(n,s,e);
    b_minlazy(n,s,e);
    b_maxlazy(n,s,e);
}
void sum_update(ll n,ll s,ll e,ll l,ll r,ll v){
    lazy(n,s,e);
    if (r<s || e<l) return;
    if (l<=s && e<=r){
        temp[n]=v;
        treeb[n]+=(e-s+1);
        if (s!=e){
        	sum_temp[n*2]+=1;
        	sum_temp[n*2+1]+=1;
		}
        lazy(n,s,e);
        return;
    }
    ll m=(s+e)/2;
    sum_update(n*2,s,m,l,r,v);
    sum_update(n*2+1,m+1,e,l,r,v);
    tree[n]=merge(tree[n*2],tree[n*2+1]);
    treeb[n]=treeb[n*2]+treeb[n*2+1];
}
void min_update(ll n,ll s,ll e,ll l,ll r,ll v){//3번 쿼리 
    lazy(n,s,e);
    if (r<s || l>e || tree[n].maxv<=v) return;
    if (l<=s && e<=r && tree[n].smax<v){
        min_temp[n]+=1;
        if (tree[n].minv==tree[n].maxv) tree[n].minv=v;
        if (tree[n].smin==tree[n].maxv) tree[n].smin=v;
        tree[n].maxv=v;
        lazy(n,s,e);
		return; 
    }
    ll m=(s+e)/2;
    min_update(n*2,s,m,l,r,v);
    min_update(n*2+1,m+1,e,l,r,v);
    tree[n]=merge(tree[n*2],tree[n*2+1]);
    treeb[n]=treeb[n*2]+treeb[n*2+1];
    return;
}
void max_update(ll n,ll s,ll e,ll l,ll r,ll v){//3번 쿼리 
    lazy(n,s,e);
    if (r<s || l>e || tree[n].minv>=v) return;
    if (l<=s && e<=r && tree[n].smin>v){
        max_temp[n]+=1;
        if (tree[n].minv==tree[n].maxv) tree[n].maxv=v;
        if (tree[n].smax==tree[n].minv) tree[n].smax=v;
        tree[n].minv=v;
        lazy(n,s,e);
        return; 
    }
    ll m=(s+e) >> 1;
    max_update(n<<1,s,m,l,r,v);
    max_update((n<<1)+1,m+1,e,l,r,v);
    tree[n]=merge(tree[n*2],tree[n*2+1]);
    treeb[n]=treeb[n*2]+treeb[n*2+1];
    return;
}
ll query(ll n,ll s,ll e,ll l,ll r){
    if (e<l || r<s) return 0ll;
    lazy(n,s,e);
    if (l<=s && e<=r) return treeb[n];
    ll m=(s+e) >> 1;
    return query(n*2,s,m,l,r)+query(n*2+1,m+1,e,l,r);
}
int main(){
    cin.tie(0);cout.tie(0);
    ios::sync_with_stdio(false);
    ll n,l;
    cin  >> n;
    for (ll i=1;i<=n;i++){
        cin >> a[i];
    }
    init(1,1,n);
	cin >> l;
    while(l--){
        ll t,q,r,k;
        cin >> t >> q >> r;
        if (t<4) cin >> k;
        if (t==1){
        	if (k!=0) sum_update(1,1,n,q,r,k);
		}
        else if (t==2)max_update(1,1,n,q,r,k);
        else if (t==3)min_update(1,1,n,q,r,k);
        else cout << query(1,1,n,q,r)<<'\n';
    }
}