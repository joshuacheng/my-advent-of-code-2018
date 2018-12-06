(ns frequency
  (:gen-class))

(defn get-cmds []
  (with-open [rdr (clojure.java.io/reader "input.txt")]
    (reduce conj [] (line-seq rdr))))
  
(defn -main [which]
  (get-cmds))
