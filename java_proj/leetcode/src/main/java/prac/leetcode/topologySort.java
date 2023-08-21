package prac.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class topologySort {
    private Map<Integer, Integer> ingreeMap;
    private List<List<Integer>> adjList;
    private int nodeNum;
    public topologySort(int numNode, List<List<Integer>> adjList) {
        this.nodeNum  = numNode;
        this.adjList = adjList;
        this.ingreeMap = IntStream.range(0, numNode).boxed()
                .collect(Collectors.toMap(x->x, x->{
                    if (x < adjList.size()) {
                        return adjList.get(x).size();
                    } else {
                        return 0;
                    }
                }));
    }
    private void dfs(List<Integer> ret, int node) {
        ret.add(node);
        // no childer for this node
        if (node >= this.adjList.size()) {
            return;
        }
        for (var ch : this.adjList.get(node)) {
            this.ingreeMap.merge(ch, -1, Integer::sum);
            if (this.ingreeMap.get(ch) == 0) {
                ret.add(node);
                dfs(ret, ch);
            }
        }
    }
    public List<Integer> findTopoOrder() {
        if (this.nodeNum != this.ingreeMap.size()) {
            return new ArrayList<>();
        }
        List<Integer> starts = this.ingreeMap.entrySet().stream()
                .filter(e -> e.getValue()==0)
                .mapToInt(Map.Entry::getKey).boxed()
                .collect(Collectors.toList());
        List<Integer> ret = new ArrayList<>();
        for (var node : starts) {
            dfs(ret, node);
        }
        if (ret.size() == this.nodeNum) {
            return ret;
        }
        return new ArrayList<>();
    }
}
