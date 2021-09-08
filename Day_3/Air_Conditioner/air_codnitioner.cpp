#include <iostream>
#include <vector>

using namespace std;

struct P {int t, a, b;};

void EX(int &a, int &b) {int t = a; a = b; b = t;}

int main() {
        ios::sync_with_stdio(0); cin.tie(0);
        int t; cin >> t;
        while (t--) {
                int n, c; cin >> n >> c;
                int pn = c;
                P pp = {0, c, c};
                bool f = true;
                while (n--) {
                        P p; cin >> p.t >> p.a >> p.b;
                        if (f) {
                                int pa = pp.a - (p.t - pp.t), pb = pp.b + (p.t - pp.t);
                                if (pa > pb) EX(pa, pb);
                                if (p.a > pb || p.b < pa) f = false;
                                pp.t = p.t;
                                pp.a = max(p.a, pa);
                                pp.b = min(p.b, pb);
                        }
                }
                if (f) cout << "YES" << endl;
                else cout << "NO" << endl;
        }
        return 0;
}