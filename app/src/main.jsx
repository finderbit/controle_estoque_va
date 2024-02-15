import React from 'react'
import ReactDOM from 'react-dom/client'



function Main() {
  return (
    <>

    </>
  )
}
const stylesHeader = {
  width: "100vw",
  height: "10vh",
  backgroundColor: "#1773cc"
}
function Header() {
  const routes = ["home", "contato"]
  return (
    <header style={stylesHeader}>
      <nav>
        {routes.map(route => (
          <a href="#">{route.toUpperCase()}</a>
        ))}
      </nav>
    </header>
  )
}

const stylesFooter = {
  display: "block",
  position: "fixed",
  height: "20vh",
}
function Footer() {
  return (
    <footer style={{
      position: "fixed",
      bottom:0,
      width: "100vw",
      backgroundColor: "#1773cc"

    }}>
      <a href="">@mateussiilva</a>
    </footer>
  )
}


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Header />
    <Main></Main>
    <Footer></Footer>
  </React.StrictMode>,
)
