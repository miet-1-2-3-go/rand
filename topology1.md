### Intro to Homology and  Cohomology
- Both are fundamental techniques used in algebraic topology
- Topology is a very flexible subject
- Continuously deforming objects are flexible due to the fact that they contain an abundance of continuous maps between two topological spaces.
  Even for very standard spaces.

Disjoin sets - Two sets are called disjoint sets if they don't have any element in common. The disjoint set data structure is used to store such sets. It supports following operations: Merging two disjoint sets to a single set using Union operation. Finding representative of a disjoint set using Find operation.
Elementary Formulations in Topology
Elementary formulations in topology focus on the foundational concepts that remain unchanged under continuous deformations. These include properties such as openness, closedness, compactness, connectedness, and separation axioms. The study of these properties helps in understanding the spatial properties of objects and their relationships. Topology provides a framework for exploring these concepts and their applications in various areas of mathematics and beyond. 
Surjectivity - A function 𝑓:𝑋→𝑌 is surjective if every element of 𝑌 is hit by at least one element of 𝑋
- It’s purely pointwise.
- It doesn’t know or care about topology, holes, paths, or connectivity.

“∀y∈Y” → for every point in 𝑌

“∃x∈X” → there exists at least one point in 𝑋 mapping to that 𝑦

Doesn’t say how many points map there — could be 1, 2, 100, or infinitely many.

Formally:

∀𝑦∈𝑌,∃𝑥∈𝑋 such that 𝑓(𝑥)=𝑦.

### T0, T1, T2, T3, and T4 Spaces
The separation axioms are fundamental concepts in topology, providing a way to classify topological spaces based on their separation properties. Here's a brief overview of each axiom:
- T0 (Kolmogorov): For any two distinct points, there exists an open set containing one point but not the other. 
- T1 (Frechet): For any two distinct points, there exist open sets containing each point but not the other. 
- T2 (Hausdorff): For any two distinct points, there exist disjoint open sets containing each point. 
- T3 (Regular): For any closed set and a point not in the set, there exist disjoint open sets containing the point and the closed set. 

- T4 (Normal): For any two disjoint closed sets, there exist disjoint open sets containing each closed set. 

An indiscrete topology on a set with more than one point is one where the only open sets are the empty set and the set itself. 
This "trivial" topology is the smallest possible topology on a given set, and consequently, any set with the indiscrete topology is not Hausdorff if it has more than one element.      .rPeykc.rWIipd{font-size:var(--m3t5);font-weight:500;line-height:var(--m3t6);margin:20px 0 10px 0}.f5cPye ul{font-size:var(--m3t7);line-height:var(--m3t8);margin:10px 0 20px 0;padding-inline-start:24px}.f5cPye .WaaZC:first-of-type ul:first-child{margin-top:0}.f5cPye ul.qh1nvc{font-size:var(--m3t7);line-height:var(--m3t8)}.f5cPye li{padding-left:4px;margin-bottom:8px;list-style:inherit}.f5cPye li.K3KsMc{list-style-type:none}.f5cPye ul>li:last-child,.f5cPye ol>li:last-child,.f5cPye ul>.bsmXxe:last-child>li,.f5cPye ol>.bsmXxe:last-child>li{margin-bottom:0}.zMgcWd{padding-bottom:16px;padding-top:8px;border-bottom:none}.dSKvsb{padding-bottom:0}li.K3KsMc .dSKvsb{margin-inline-start:-28px}.GmFi7{display:flex;width:100%}.f5cPye li:first-child .zMgcWd{padding-top:0}.f5cPye li:last-child .zMgcWd{border-bottom:none;padding-bottom:0}.xFTqob{flex:1;min-width:0}.Gur8Ad{font-size:var(--m3t11);font-weight:500;line-height:var(--m3t12);overflow:hidden;padding-bottom:4px;transition:transform 200ms cubic-bezier(0.20,0.00,0.00,1.00)}.vM0jzc{color:var(--m3c9);font-size:var(--m3t7);line-height:var(--m3t8)}.vM0jzc ul,.vM0jzc ol{font-size:var(--m3t7) !important;line-height:var(--m3t8) !important;margin-top:8px !important}.vM0jzc li ul,.vM0jzc li ol{font-size:var(--m3t9) !important;letter-spacing:0.1px !important;line-height:var(--m3t10) !important;margin-top:0 !important}.vM0jzc ul li{list-style-type:disc}.vM0jzc ui li li{list-style-type:circle}.vM0jzc .rPeykc:first-child{margin-top:0}.CM8kHf text{fill:var(--m3c11)}.CM8kHf{font-size:1.15em}.j86kh{display:inline-block;max-width:100%}          Properties of an indiscrete topology with more than one point     Only two open sets: The collection of open sets is \(\tau =\{\emptyset ,X\}\), where \(X\) is the set.  Not Hausdorff: If a topological space has more than one element, it is not Hausdorff because any two distinct points cannot have disjoint neighborhoods.  Compact: The space is always compact, meaning every open cover has a finite subcover.  Separable: The space is separable. This is because the set itself is a countable dense subset.  Second countable: The indiscrete topology is second countable because the collection of open sets \(\{\emptyset ,X\}\) is a countable basis. 

These axioms have significant implications for various areas of mathematics, including compactness, connectedness, and analysis. 
The separation axioms are related to each other in a hierarchical structure, with some axioms implying others. 
For example, a T4 space is a T1 space that is normal, and a T5 space is a T4 space that is completely normal. 

X - input world, you start from here
Y - output work, receives result (x) from f
V - a region of Y we care about
