import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

export default function NotesApp() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [tag, setTag] = useState("");
  const [notes, setNotes] = useState([]);

  const fetchNotes = async () => {
    const res = await fetch("http://localhost:8000/notes/");
    const data = await res.json();
    setNotes(data);
  };

  const handleCreate = async () => {
    const res = await fetch("http://localhost:8000/notes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title, content, tag }),
    });
    if (res.ok) {
      setTitle("");
      setContent("");
      setTag("");
      fetchNotes();
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  return (
    <div className="p-6 space-y-6">
      <Card>
        <CardContent className="space-y-4 pt-6">
          <h2 className="text-xl font-bold">Create a New Note</h2>
          <Input
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <Textarea
            placeholder="Content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
          <Input
            placeholder="Tag (optional)"
            value={tag}
            onChange={(e) => setTag(e.target.value)}
          />
          <Button onClick={handleCreate}>Create Note</Button>
        </CardContent>
      </Card>

      <div className="space-y-4">
        <h2 className="text-xl font-bold">All Notes</h2>
        {notes.map((note) => (
          <Card key={note.id}>
            <CardContent className="pt-4">
              <h3 className="font-semibold">{note.title} (v{note.version})</h3>
              <p className="text-sm text-gray-600">{note.tag}</p>
              <p className="mt-2 whitespace-pre-wrap">{note.content}</p>
              <p className="text-xs text-gray-400 mt-2">{note.timestamp}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
