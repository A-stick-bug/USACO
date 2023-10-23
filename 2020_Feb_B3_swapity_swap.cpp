// Reusing code from 2020 Feb Silver 1: Swapity Swapity Swap
//
// for each cow, find where it will be after K iterations
// note: it is guaranteed that after some number of iterations, it will end up back at its original location
// in other words, we know that every cow is in exactly 1 cycle
// use dfs to find elements in each cycle and its length, handle each cycle separately

#include <bits/stdc++.h>

using namespace std;

const int MN = 100001;
int cows[MN], dist[MN], res[MN];
vector<int> path;

int dfs(int cur, int d) {
    if (dist[cur] != -1) {
        return d - dist[cur];
    }
    dist[cur] = d;
    path.push_back(cur);  // keep track of elements in the current path
    return dfs(cows[cur], d + 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K, M = 2;
    cin >> N >> K;
    for (int i = 1; i <= N; i++)  // create initial state
        cows[i] = i;

    int a, b;
    for (int i = 0; i < M; i++) {  // create 'graph' based on what we reverse
        cin >> a >> b;
        reverse(begin(cows) + a, begin(cows) + b + 1);
    }

    for (int i = 1; i <= N; i++)  // fill with -1
        dist[i] = -1;

    for (int i = 1, length; i <= N; i++) {
        path.clear();
        if (dist[i] == -1) {  // not processed yet, get cycle length and elements in cycle
            length = dfs(i, 0);

            for (int j = 0; j < length; j++)  // find where each cow in this cycle ends up after K moves
                res[path[j]] = path[(j + K) % length];  // mod length because cycles bring you back to the same place
        }
    }

    for (int i = 1; i <= N; i++) {  // output results in order
        cout << res[i] << "\n";
    }

    return 0;
}
