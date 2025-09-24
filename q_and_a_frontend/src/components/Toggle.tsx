import React from "react";

type Props = {
  checked: boolean;
  onChange: (checked: boolean) => void;
  label?: string;
};

export function Toggle({ checked, onChange, label }: Props) {
  return (
    <label style={{ display: "inline-flex", alignItems: "center", gap: 10, cursor: "pointer" }}>
      <div
        role="switch"
        aria-checked={checked}
        tabIndex={0}
        onClick={() => onChange(!checked)}
        onKeyDown={(e) => {
          if (e.key === " " || e.key === "Enter") {
            e.preventDefault();
            onChange(!checked);
          }
        }}
        style={{
          width: 44,
          height: 26,
          background: checked ? "var(--primary)" : "rgba(0,0,0,0.2)",
          borderRadius: 9999,
          position: "relative",
          transition: "background 0.2s ease",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: 3,
            left: checked ? 22 : 3,
            width: 20,
            height: 20,
            borderRadius: "50%",
            background: "#fff",
            boxShadow: "var(--shadow-sm)",
            transition: "left 0.2s ease",
          }}
        />
      </div>
      {label && <span style={{ fontSize: 14 }}>{label}</span>}
    </label>
  );
}
