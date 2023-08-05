import ListGroup from "./components/ListGroup";

function App() {
  let items = ["Houston", "Paris", "Austin", "San Antonio", "Santo Domingo", "San Salvador"] 
  
  const handleSelectItem = (item: string) => {
    console.log(item);
  }
  
  return (
    <div>
      <ListGroup items={items} heading="Cities" onSelectItem={handleSelectItem}/>
    </div>
  );
}

export default App;