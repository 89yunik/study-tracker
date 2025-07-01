import styles from "./ArrayTutorial.module.css"

export const ArrayTutorial = () => {
  return (
    <div className={styles.container}>
      {Array.from({ length: 5 }).map((_, index) => (
        <div key={index}>{index}</div>
      ))}
    </div>
  )
}
