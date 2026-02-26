function Button({ children, style }) {
  return <button style={style}>{children}</button>;
}

function PrimaryButton(props) {
  return (
    <Button
      {...props}
      style={{ backgroundColor: "blue", color: "white" }}
    />
  );
}

function DangerButton(props) {
  return (
    <Button
      {...props}
      style={{ backgroundColor: "red", color: "white" }}
    />
  );
}