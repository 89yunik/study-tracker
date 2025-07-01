import { useEffect, useState } from "react"
import { ArrayTutorial } from "./ArrayTutorial"

const App = () => {
  const [count, setCount] = useState(0)
  //   useEffect(() => {
  //     const timeout = setTimeout(() => {
  //       setCount((prev) => {
  //         return prev + 1
  //       })
  //     }, 100)
  //     return () => clearTimeout(timeout) // 없으면 메모리 누수
  //   }, [])

  // functional update(함수형 업데이트)
  // react의 생명 주기
  useEffect(() => {
    const timeout = setTimeout(() => {
      setCount(count + 1)
    }, 1000)

    // window.addEventListener('click', () => {})
    // return () => window.removeEventListener('click',handleclick)

    return () => clearTimeout(timeout) // 없으면 메모리 누수
  }, [count])

  return (
    <div>
      <div>{count}</div>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <ArrayTutorial />
    </div>
  )
}

export default App
