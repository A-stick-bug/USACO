#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


class LCA {
public:
    vector<int> depth;
    vector<int> first;
    vector<int> euler;
    vector<vector<pair<int, int>>> st;
    vector<vector<int>> graph;
    int N;

    LCA(int n, vector<vector<int>> &g) {
        N = n;
        depth.resize(N);
        first.resize(N);
        graph = g;
        dfs(0, -1);
        int M = euler.size();
        int LOG = log2(M);
        st.resize(2 * N, vector<pair<int, int>>(18));
        for (int i = 0; i < M; i++) {
            st[i][0] = make_pair(depth[euler[i]], euler[i]);
        }
        for (int k = 1; k <= LOG; k++) {
            for (int i = 0; i < M - (1 << k) + 1; i++) {
                st[i][k] = min(st[i][k - 1], st[i + (1 << (k - 1))][k - 1]);
            }
        }
    }

    void dfs(int u, int prev) {
        first[u] = euler.size();
        euler.push_back(u);
        for (int v: graph[u]) {
            if (v != prev) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
                euler.push_back(u);
            }
        }
    }

    int lca(int u, int v) {
        int left = min(first[u], first[v]);
        int right = max(first[u], first[v]);
        int k = log2(right - left + 1);
        return min(st[left][k], st[right - (1 << k) + 1][k]).second;
    }
};

const int NN = 100010;
vector<int> cows(NN);
vector<vector<int>> graph(NN);
vector<int> h_cow(NN);

void h_cows(int cur, int prev) {
    for (int adj: graph[cur]) {
        if (adj == prev) continue;
        h_cow[adj] = h_cow[cur] + cows[adj];
        h_cows(adj, cur);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int Q, N;
    cin >> N >> Q;

    for (int i = 0; i < N; i++) {
        char c;
        cin >> c;
        cows[i] = (c == 'H' ? 1 : 0);
    }

    for (int i = 1; i < N; i++) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }


    h_cow[0] = cows[0];
    h_cows(0, -1);

    LCA tree(N, graph);
    for (int i = 0; i < Q; i++) {
        string q;
        int u, v;
        cin >> u >> v >> q;
        u--;
        v--;
        int ancestor = tree.lca(u, v);
        int h_nodes = h_cow[u] + h_cow[v] - 2 * h_cow[ancestor] + cows[ancestor];
        int total_nodes = tree.depth[u] + tree.depth[v] - 2 * tree.depth[ancestor] + 1;
        if ((q == "H" && h_nodes) || (q == "G" && total_nodes != h_nodes)) {
            cout << 1;
        } else {
            cout << 0;
        }
    }
    cout << endl;
    return 0;
}


